def fetch_corrections(assignment_id):
  import base64, datetime, json, pytz
  from urllib.request import urlopen
  from IPython.display import display, Markdown
  def fetch_github(gh_url):
    md_data = json.load(urlopen(gh_url))
    md_content_b64 = md_data['content']
    md_content = base64.b64decode(md_content_b64).decode('utf-8')
    return md_content
  exec_timestamp = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S %Z")
  corrections_url = f"https://api.github.com/repos/jpowerj/dsan-content/contents/2026-sum-dsan5650/DSAN5650_{assignment_id}_Corrections.md?ref=main"
  md_content = fetch_github(corrections_url)
  corrections_content = md_content + f"\n\nLast fetched: {exec_timestamp}"
  display(Markdown(corrections_content))

def gen_hint_button(assignment_id):
  import datetime, getpass, ipylab, ipywidgets, IPython.display, pytz, time
  from redis import Redis
  from rq import Queue
  jfe = ipylab.JupyterFrontEnd()
  button = ipywidgets.Button(
    description=f'Get Hints for {assignment_id}',
    layout=ipywidgets.Layout(width='250px')
  )
  output = ipywidgets.Output()
  IPython.display.display(button, output)

  def _generate_timestamp(datetime_obj):
    return str(datetime_obj).split(".")[0].replace(" ","_").replace(":","").replace("-","")

  def _get_elapsed(t0):
    elapsed_delta = datetime.datetime.now() - t0
    return elapsed_delta.seconds
  
  def _on_button_clicked(b):
    with output: print("Saving notebook...")
    jfe.commands.execute('docmanager:save')
    time.sleep(0.2)
    cur_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
    cur_ts = _generate_timestamp(cur_time)
    output.clear_output()
    with output: print(f"Getting hints for assignment (hint submission timestamp {cur_ts})...")
    username = getpass.getuser()
    netid = username.replace("jupyter-","")
    q = Queue(connection=Redis())
    enqueue_time = datetime.datetime.now()
    jah_job = q.enqueue("jahtask.grade_user", "DSAN5650", assignment_id, username, cur_ts)
    time.sleep(0.2)
    while jah_job.is_queued:
        output.clear_output()
        elapsed = _get_elapsed(enqueue_time)
        with output: print(f"Notebook in queue (elapsed time: {str(elapsed)})...")
        time.sleep(0.5)
    while jah_job.is_started:
        output.clear_output()
        elapsed = _get_elapsed(enqueue_time)
        with output: print(f"Notebook execution started (elapsed time: {str(elapsed)})...")
        time.sleep(1)
    if jah_job.is_finished:
        output.clear_output()
        elapsed = _get_elapsed(enqueue_time)
        result_fpath = f'{assignment_id}/feedback/{netid}_{assignment_id}_{cur_ts}.html'
        with output: print(f"Hint report complete! Opening {result_fpath}...")
        jfe.commands.execute('docmanager:open-browser-tab', args={'path': result_fpath})
    else:
        output.clear_output()
        with output: print(f"AutoHinter error (please retry, and if the issue persists, email dsan5650-staff@georgetown.edu)")
  
  button.on_click(_on_button_clicked)

def gen_submit_button(assignment_id):
  import datetime, getpass, ipylab, ipywidgets, IPython.display, pathlib, pytz, shutil, time
  jfe = ipylab.JupyterFrontEnd()
  button = ipywidgets.Button(
    description=f'Submit {assignment_id} for Grading',
    layout=ipywidgets.Layout(width='250px'),
  ) 
  output = ipywidgets.Output()
  IPython.display.display(button, output)

  def _generate_timestamp(datetime_obj):
    return str(datetime_obj).split(".")[0].replace(" ","_").replace(":","").replace("-","")
  
  def _on_button_clicked(b):
    with output: print("Saving notebook...")
    jfe.commands.execute('docmanager:save')
    time.sleep(0.2)
    cur_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
    cur_ts = _generate_timestamp(cur_time)
    output.clear_output()
    with output: print(f"Submitting assignment (submission timestamp {cur_ts})...")
    username = getpass.getuser()
    netid = username.replace("jupyter-","")
    # And copy
    notebook_fname = f'DSAN5650_{assignment_id}.ipynb'
    source_fpath = f'/home/{username}/{assignment_id}/{notebook_fname}'
    dest_notebook_suffix = notebook_fname.replace(".ipynb",f'_{cur_ts}.ipynb')
    dest_notebook_fname = f'{netid}_{dest_notebook_suffix}'
    submission_root = f'/home/{username}/submissions/{assignment_id}'
    pathlib.Path(submission_root).mkdir(parents=True, exist_ok=True)
    target_fpath = f'{submission_root}/{dest_notebook_fname}'
    shutil.copy(source_fpath, target_fpath)
    # Completion message
    output.clear_output()
    with output: print(f"Assignment submitted! Instructors now have a copy, {dest_notebook_fname}, that will be used for grading.")
  
  button.on_click(_on_button_clicked)
