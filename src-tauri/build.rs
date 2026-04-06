use std::fs;
use std::process::Command;

fn main() {
    if std::env::var("PROFILE").unwrap() == "release" {
  
        let python_path = if std::path::Path::new("../backend/venv/Scripts/python.exe").exists() {
            "../backend/venv/Scripts/python.exe"
        } else {
            "python" // fallback
        };

        let output = Command::new(python_path)
            .arg("-m")
            .arg("PyInstaller")
            .arg("--onefile")
            .arg("--noconsole")
            .arg("../backend/main.py")
            .output()
            .expect("Failed to run PyInstaller");

        if !output.status.success() {
            let err = String::from_utf8_lossy(&output.stderr);
            panic!("Build failed: {}", err);
        }

        let target = std::env::var("TARGET").unwrap();
        let sidecar_filename = format!("binaries/main-{}.exe", target);

        fs::create_dir_all("binaries").expect("Failed to create binaries directory");
        fs::copy("dist/main.exe", &sidecar_filename).expect("Failed to copy exe");

    }
    tauri_build::build();
}
