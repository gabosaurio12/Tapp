#!/bin/bash

pg_restore -U your_user -d database_name -v "Construction/TaskManager/database/task_manager_db.dump"

pyinstaller --name "Tapp" --onefile --windowed --icon=MyIcon.icns --add-data "resources:resources" Construction/TaskManager/src/main.py

cp dist/Tapp.app /Applications/