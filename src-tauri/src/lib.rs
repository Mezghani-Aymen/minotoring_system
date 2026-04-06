#[cfg_attr(mobile, tauri::mobile_entry_point)]
mod data_service;
mod env_utils;
mod file_utils;
mod process_utils;
mod python_commands;
mod theme;

use crate::process_utils::stop_python;
use crate::python_commands::PythonState;
use tauri::{Manager, RunEvent};

pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .plugin(tauri_plugin_notification::init())
        .invoke_handler(tauri::generate_handler![
            theme::switch_theme,
            data_service::fetch_aggregated_data,
            python_commands::run_python,
            python_commands::is_python_running
        ])
        .manage(python_commands::PythonState {
            child: std::sync::Mutex::new(None),
        })
        .setup(|app| {
            use tauri_plugin_notification::NotificationExt;
            app.notification()
                .builder()
                .title("Monitoring System")
                .body("The app is running")
                .show()
                .unwrap();

            app.handle().plugin(
                tauri_plugin_log::Builder::default()
                    .level(log::LevelFilter::Info)
                    .build(),
            )?;
            Ok(())
        })
        .build(tauri::generate_context!())
        .expect("error while building tauri application")
        .run(|app_handle, event| match event {
            RunEvent::ExitRequested { .. } | RunEvent::Exit => {
                log::info!(">>> App exiting (handler: {:?})", event);
                let state = app_handle.state::<PythonState>();
                stop_python(app_handle, &state);
            }
            _ => {}
        });
}
