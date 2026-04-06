use crate::process_utils::{
    build_command, is_process_running, store_process,
};
use std::sync::Mutex;
use tauri::{AppHandle, State, Manager};
use tauri_plugin_shell::process::{CommandChild, CommandEvent};

pub struct PythonState {
    pub child: Mutex<Option<CommandChild>>,
}

#[tauri::command]
pub fn is_python_running(state: State<'_, PythonState>) -> bool {
    let lock = state.child.lock().unwrap();
    is_process_running(&*lock)
}

#[tauri::command]
pub fn run_python(app: AppHandle, state: State<'_, PythonState>) -> Result<String, String> {
    use crate::env_utils::set_envs;
    use crate::file_utils::{ensure_directories, get_base_path, prepare_paths};
    use tauri::Emitter;

    // 1. Check running
    {
        let lock = state.child.lock().unwrap();
        if is_process_running(&*lock) {
            return Ok("Monitoring System Already Running".to_string());
        }
    }

    // 2. Paths
    let base_path = get_base_path(&app)?;
    let (raw_path, aggregated_path) = prepare_paths(&base_path);

    // 3. Ensure dirs
    ensure_directories(&raw_path, &aggregated_path)?;

    // 4. Build command
    let is_dev = cfg!(debug_assertions);
    let mut cmd = build_command(&app, is_dev)?;

    // 5. Env variables
    cmd = set_envs(cmd, is_dev, &base_path, &raw_path, &aggregated_path);

    // 6. Spawn
    let (mut rx, child) = match cmd.spawn() {
        Ok(c) => c,
        Err(e) => {
            let _ = app.emit("python-log", format!("ERROR: Spawning failed: {}", e));
            return Err(e.to_string());
        }
    };

    // 7. Store
    store_process(&state, child);

    // 8. Capture events
    let app_handle = app.clone();
    tauri::async_runtime::spawn(async move {
        while let Some(event) = rx.recv().await {
            match event {
                CommandEvent::Stdout(line) => {
                    let msg = String::from_utf8_lossy(&line).into_owned();
                    let _ = app_handle.emit("python-log", msg);
                }
                CommandEvent::Stderr(line) => {
                    let msg = String::from_utf8_lossy(&line).into_owned();
                    let _ = app_handle.emit("python-log", format!("ERROR: {}", msg));
                }
                CommandEvent::Terminated(payload) => {
                    let msg = format!("Process terminated with code: {:?}", payload.code);
                    let _ = app_handle.emit("python-log", msg);
                    
                    if let Some(app_state) = app_handle.try_state::<PythonState>() {
                        let mut lock = app_state.child.lock().unwrap();
                        *lock = None;
                    }
                }
                _ => {}
            }
        }
    });

    Ok("Monitoring System Started in Background".to_string())
}
