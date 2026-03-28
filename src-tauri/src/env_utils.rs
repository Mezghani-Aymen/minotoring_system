use std::{path::PathBuf, process::Command};

pub fn set_envs(
    cmd: &mut Command,
    is_dev: bool,
    base: &PathBuf,
    raw: &PathBuf,
    aggregated: &PathBuf,
) {
    cmd.env("APP_MODE", if is_dev { "dev" } else { "prod" });
    cmd.env("APP_DATA_DIR", base.to_string_lossy().to_string());
    cmd.env("RAW_FILE_PATH", raw.to_string_lossy().to_string());
    cmd.env("AGGREGATED_FILE_PATH", aggregated.to_string_lossy().to_string());
}