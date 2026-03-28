#[tauri::command]
pub fn fetch_aggregated_data(app: tauri::AppHandle, date: String) -> Result<String, String> {
    use crate::file_utils;
    use std::fs;

    let base_path = file_utils::get_base_path(&app)?;
    let mut path = base_path.join("aggregated");

    path.push(format!("aggregated_{}.json", date));

    match fs::read_to_string(&path) {
        Ok(data) => Ok(data),
        Err(e) => Err(format!("Error reading file at {:?}: {}", path, e)),
    }
}