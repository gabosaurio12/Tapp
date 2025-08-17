#!/bin/bash

pg_restore -U your_user -d database_name -v "Construction/TaskManager/database/task_manager_db.dump"

cd Construction/TaskManager/src

pyinstaller --name "Tapp" --onefile --windowed --icon=MyIcon.icns --add-data "resources:resources" main.py

ditto dist/Tapp.app /Applications/Tapp.app

cd .. && cd .. && cd ..