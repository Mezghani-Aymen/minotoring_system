use std::path::PathBuf;
use tauri_plugin_shell::process::Command;

pub fn set_envs(
    cmd: Command,
    is_dev: bool,
    base: &PathBuf,
    raw: &PathBuf,
    aggregated: &PathBuf,
) -> Command {
    cmd.env("APP_MODE", if is_dev { "dev" } else { "prod" })
        .env("APP_DATA_DIR", base.to_string_lossy().to_string())
        .env("RAW_FILE_PATH", raw.to_string_lossy().to_string())
        .env("AGGREGATED_FILE_PATH", aggregated.to_string_lossy().to_string())
}