use std::process::{Child, Command};
use tauri::State;
use crate::python_commands::PythonState;

pub fn check_and_cleanup_process(lock: &mut Option<Child>) -> bool {
    if let Some(child) = lock.as_mut() {
        match child.try_wait() {
            Ok(None) => true, // Still running!
            _ => {
                // The process finished, crashed, or errored.
                // We set it to None to clear the memory.
                *lock = None;
                false
            }
        }
    } else {
        false // Nothing was ever running
    }
}

pub fn spawn_process(cmd: &mut Command) -> Result<Child, String> {
    cmd.spawn()
        .map_err(|e| format!("Failed to spawn process: {}", e))
}

pub fn store_process(state: &State<'_, PythonState>, child: Child) {
    let mut lock = state.child.lock().unwrap();
    *lock = Some(child);
}
