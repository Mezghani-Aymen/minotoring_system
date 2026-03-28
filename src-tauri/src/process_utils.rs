use std::process::Child;

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