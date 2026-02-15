use tauri::{Theme, Window};

#[tauri::command]
pub fn switch_theme(window: Window, theme: String) {
    match theme.as_str() {
        "dark" => window.set_theme(Some(Theme::Dark)).unwrap(),
        "light" => window.set_theme(Some(Theme::Light)).unwrap(),
        "system" => window.set_theme(None).unwrap(), // Follows OS theme
        _ => {}
    }
}