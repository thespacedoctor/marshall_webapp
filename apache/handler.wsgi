
import os
import sys
import atexit
import time

import mod_wsgi.server

working_directory = '/misc/pessto/git_repos/marshall_webapp'
python_paths = None

entry_point = '/misc/pessto/git_repos/marshall_webapp/production_qubvm.wsgi'
application_type = 'script'
callable_object = 'application'
mount_point = '/'
with_newrelic_agent = False
newrelic_config_file = ''
newrelic_environment = ''
reload_on_changes = False
debug_mode = False
enable_debugger = False
debugger_startup = False
enable_coverage = False
coverage_directory = ''
enable_profiler = False
profiler_directory = ''
enable_recorder = False
recorder_directory = ''

if python_paths:
    sys.path.extend(python_paths)

if debug_mode:
    # We need to fiddle sys.path as we are not using daemon mode and so
    # the working directory will not be added to sys.path by virtue of
    # 'home' option to WSGIDaemonProcess directive. We could use the
    # WSGIPythonPath directive, but that will cause .pth files to also
    # be evaluated.

    sys.path.insert(0, working_directory)

def output_coverage_report():
    coverage_info.stop()
    coverage_info.html_report(directory=coverage_directory)

if enable_coverage:
    from coverage import coverage
    coverage_info = coverage()
    coverage_info.start()
    atexit.register(output_coverage_report)

def output_profiler_data():
    profiler_info.disable()
    output_file = '%s-%d.pstats' % (int(time.time()*1000000), os.getpid())
    output_file = os.path.join(profiler_directory, output_file)
    profiler_info.dump_stats(output_file)

if enable_profiler:
    from cProfile import Profile
    profiler_info = Profile()
    profiler_info.enable()
    atexit.register(output_profiler_data)

if with_newrelic_agent:
    if newrelic_config_file:
        os.environ['NEW_RELIC_CONFIG_FILE'] = newrelic_config_file
    if newrelic_environment:
        os.environ['NEW_RELIC_ENVIRONMENT'] = newrelic_environment

handler = mod_wsgi.server.ApplicationHandler(entry_point,
        application_type=application_type, callable_object=callable_object,
        mount_point=mount_point, with_newrelic_agent=with_newrelic_agent,
        debug_mode=debug_mode, enable_debugger=enable_debugger,
        debugger_startup=debugger_startup, enable_recorder=enable_recorder,
        recorder_directory=recorder_directory)

reload_required = handler.reload_required
handle_request = handler.handle_request

if reload_on_changes and not debug_mode:
    mod_wsgi.server.start_reloader()

