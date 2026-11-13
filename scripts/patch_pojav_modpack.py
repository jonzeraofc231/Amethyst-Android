from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
layout = root / "app_pojavlauncher/src/main/res/layout/fragment_launcher.xml"
main = root / "app_pojavlauncher/src/main/java/net/kdt/pojavlaunch/fragments/MainMenuFragment.java"

layout_text = layout.read_text(encoding="utf-8")
old_layout = """\t\t\t<com.kdt.mcgui.LauncherMenuButton
\t\t\t\tandroid:id="@+id/open_files_button"
\t\t\t\tstyle="@style/LauncherMenuButton.Universal"
\t\t\t\tandroid:layout_width="match_parent"
\t\t\t\tandroid:drawableStart="@drawable/ic_px_folder"
\t\t\t\tandroid:text="@string/mcl_button_open_directory"
\t\t\t\tapp:layout_constraintTop_toBottomOf="@id/share_logs_button" />"""
new_layout = old_layout + """

\t\t\t<com.kdt.mcgui.LauncherMenuButton
\t\t\t\tandroid:id="@+id/install_modpack_button"
\t\t\t\tstyle="@style/LauncherMenuButton.Universal"
\t\t\t\tandroid:layout_width="match_parent"
\t\t\t\tandroid:drawableStart="@drawable/ic_px_java_run"
\t\t\t\tandroid:text="@string/import_local_modpack"
\t\t\t\tapp:layout_constraintTop_toBottomOf="@id/open_files_button" />"""
if old_layout not in layout_text:
    raise SystemExit("Open game directory block not found")
layout.write_text(layout_text.replace(old_layout, new_layout, 1), encoding="utf-8")

main_text = main.read_text(encoding="utf-8")
bind_old = "        Button mOpenDirectoryButton = view.findViewById(R.id.open_files_button);"
bind_new = bind_old + "\n        Button mInstallModpackButton = view.findViewById(R.id.install_modpack_button);"
if bind_old not in main_text:
    raise SystemExit("Open directory binding not found")
main_text = main_text.replace(bind_old, bind_new, 1)

click_old = "        mOpenDirectoryButton.setOnClickListener((v)-> openGameDirectory(v.getContext()));"
click_new = click_old + """

        mInstallModpackButton.setOnClickListener(v ->
                Tools.swapFragment(requireActivity(), SearchModFragment.class,
                        SearchModFragment.TAG, null));"""
if click_old not in main_text:
    raise SystemExit("Open directory click handler not found")
main.write_text(main_text.replace(click_old, click_new, 1), encoding="utf-8")

print("PojavLauncher modpack button patch applied.")
