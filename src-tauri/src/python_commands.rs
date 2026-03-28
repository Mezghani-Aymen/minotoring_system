use crate::process_utils::check_and_cleanup_process;
use std::process::Child;
use std::sync::Mutex;
use tauri::State;

pub struct PythonState {
    pub child: Mutex<Option<Child>>, // Option<Child> ==> {Return: Some(process) → Python is running / None → Python is NOT running}
}

#[tauri::command]
pub fn is_python_running(state: State<'_, PythonState>) -> bool {
    let mut lock = state.child.lock().unwrap();
    check_and_cleanup_process(&mut *lock)
}
