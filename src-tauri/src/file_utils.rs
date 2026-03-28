use std::path::PathBuf;
use tauri::{AppHandle, Manager};

pub fn get_base_path(app: &AppHandle) -> Result<std::path::PathBuf, String> {
    let is_dev = cfg!(debug_assertions);
    if is_dev {
        Ok(std::path::PathBuf::from("../backend/data/"))
    } else {
        app.path().app_data_dir().map_err(|e| e.to_string())
    }
}

pub fn prepare_paths(base_path: &PathBuf) -> (PathBuf, PathBuf) {
    let raw = base_path.join("raw/");
    let aggregated = base_path.join("aggregated/");
    (raw, aggregated)
}
