use std::fs;
use std::process::Command;

fn main() {
    println!("cargo:rerun-if-changed=../backend/main.py");

    if std::env::var("PROFILE").unwrap() == "release" {
        println!(">>> Building Python EXE...");

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

        println!(">>> Copying EXE...");

        fs::create_dir_all("resources/backend").expect("Failed to create resources directory");

        fs::copy("dist/main.exe", "resources/backend/main.exe").expect("Failed to copy exe");

        println!(">>> Python EXE ready!");
    } else {
        println!(">>> Skipping Python build (dev mode)");
    }

    tauri_build::build();
}
