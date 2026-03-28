#[cfg_attr(mobile, tauri::mobile_entry_point)]
mod data_service;
mod env_utils;
mod file_utils;
mod process_utils;
mod python_commands;
mod theme;

pub fn run() {
    // TODO: Add stop tracking when i close app.
    tauri::Builder::default()
        .plugin(tauri_plugin_notification::init())
        .invoke_handler(tauri::generate_handler![theme::switch_theme])
        .setup(|app| {
            use tauri_plugin_notification::NotificationExt;
            app.notification()
                .builder()
                .title("Monitoring System")
                .body("The app is running")
                .show()
                .unwrap();

            if cfg!(debug_assertions) {
                app.handle().plugin(
                    tauri_plugin_log::Builder::default()
                        .level(log::LevelFilter::Info)
                        .build(),
                )?;
            }
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
