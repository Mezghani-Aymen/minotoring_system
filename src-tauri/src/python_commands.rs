use crate::process_utils::{
    build_command, check_and_cleanup_process, spawn_process, store_process,
};
use std::process::Child;
use std::sync::Mutex;
use tauri::{AppHandle, State};

pub struct PythonState {
    pub child: Mutex<Option<Child>>, // Option<Child> ==> {Return: Some(process) → Python is running / None → Python is NOT running}
}

#[tauri::command]
pub fn is_python_running(state: State<'_, PythonState>) -> bool {
    let mut lock = state.child.lock().unwrap();
    check_and_cleanup_process(&mut *lock)
}

#[tauri::command]
pub fn run_python(app: AppHandle, state: State<'_, PythonState>) -> Result<String, String> {
    use crate::env_utils::set_envs;
    use crate::file_utils::{ensure_directories, get_base_path, prepare_paths};

    // 1. Check running
    {
        let mut lock = state.child.lock().unwrap();
        if check_and_cleanup_process(&mut *lock) {
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
    set_envs(&mut cmd, is_dev, &base_path, &raw_path, &aggregated_path);

    // 6. Spawn
    let mut child = match spawn_process(&mut cmd) {
        Ok(c) => c,
        Err(e) => {
            let _ = app.emit("python-log", format!("ERROR: Spawning failed: {}", e));
            return Err(e);
        }
    };

    // 7. Store
    store_process(&state, child);

    Ok("Monitoring System Started in Background".to_string())
}
