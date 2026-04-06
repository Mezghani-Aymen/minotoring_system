use crate::python_commands::PythonState;
use tauri::{AppHandle, State};
use tauri_plugin_shell::process::{Command, CommandChild};
use tauri_plugin_shell::ShellExt;

pub fn is_process_running(lock: &Option<CommandChild>) -> bool {
    lock.is_some()
}

pub fn store_process(state: &State<'_, PythonState>, child: CommandChild) {
    let mut lock = state.child.lock().unwrap();
    *lock = Some(child);
}

pub fn build_command(app: &AppHandle, is_dev: bool) -> Result<Command, String> {
    if is_dev {
        let cmd = app
            .shell()
            .command("../backend/venv/Scripts/python.exe")
            .args(&["../backend/main.py"]);
        Ok(cmd)
    } else {
        let sidecar = app
            .shell()
            .sidecar("main")
            .map_err(|e| format!("Failed to create sidecar command: {}", e))?;
        Ok(sidecar)
    }
}

pub fn stop_python(_app_handle: &AppHandle, state: &State<'_, PythonState>) {
    let mut lock = state.child.lock().unwrap();
    if let Some(child) = lock.take() {
        let pid = child.pid();
        
        #[cfg(target_os = "windows")]
        {
            let _ = std::process::Command::new("taskkill")
                .args(&["/F", "/T", "/PID", &pid.to_string()])
                .status();
            log::info!("Python process tree {} stopped via taskkill.", pid);
        }

        let _ = child.kill();
    }
}
