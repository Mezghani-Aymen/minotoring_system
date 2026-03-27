use std::process::Child;
use std::sync::Mutex;
use tauri::State;

pub struct PythonState {
    pub child: Mutex<Option<Child>>, // Option<Child> ==> {Return: Some(process) → Python is running / None → Python is NOT running}
}

#[tauri::command]
pub fn is_python_running(state: State<'_, PythonState>) -> bool {
    let mut lock = state.child.lock().unwrap();
    if let Some(child) = lock.as_mut() {
        match child.try_wait() {
            Ok(None) => true, // Still running
            Ok(Some(_)) => {
                *lock = None; // Process exited
                false
            }
            Err(_) => false,
        }
    } else {
        false
    }
}