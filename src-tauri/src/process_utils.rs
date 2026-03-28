use std::process::{Child, Command};

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

fn spawn_process(cmd: &mut Command) -> Result<Child, String> {
    cmd.spawn().map_err(|e| format!("Failed to spawn process: {}", e))
}