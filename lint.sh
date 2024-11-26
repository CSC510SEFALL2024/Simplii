#!/bin/sh
autopep8 --in-place --aggressive src/application.py
echo "src/application.py complete"
autopep8 --in-place --aggressive src/apps.py
echo "src/apps.py complete"
autopep8 --in-place --aggressive src/test/tests.py
echo "src/test/tests.py complete"
autopep8 --in-place --aggressive src/forms/user_forms.py
echo "src/forms/user_forms.py complete"
autopep8 --in-place --aggressive src/forms/task_forms.py
echo "src/forms/task_forms.py complete"
autopep8 --in-place --aggressive src/forms/job_forms.py
echo "src/forms/job_forms.py complete"
autopep8 --in-place --aggressive src/forms/validators.py
echo "src/forms/validators.py complete"
autopep8 --in-place --aggressive src/forms/base_fields.py
echo "src/forms/base_fields.py complete"
autopep8 --in-place --aggressive models/recommend.py
echo "models/recommend.py complete"
autopep8 --in-place --aggressive models/stats.py
echo "models/stats.py complete"
