---
title: "Jupyterlab With System Monitor"
date: 2020-11-28T21:33:42+08:00

Categories:
  - coding
---

![alt](https://raw.githubusercontent.com/jtpio/jupyterlab-system-monitor/main/doc/screencast.gif)

Try to switch to jupterlab, the cpu/mem graph looks greeeat. https://github.com/jtpio/jupyterlab-system-monitor

But install n-times, the graph still no showing.

Thanks my colleague Bill, indicate the version issue of nbresuse

Reinstall the package, finally works!

```sh
$ brew install node
$ pip install jupyterlab
$ pip install nbresuse==0.3.6
$ jupyter labextension install jupyterlab-topbar-extension jupyterlab-system-monitor
$ jupyter notebook --generate-config
```

Generate the jupyter config and fill the display config

```yaml
c.NotebookApp.ResourceUseDisplay.mem_limit = 16 * 1024 ** 3
c.NotebookApp.ResourceUseDisplay.track_cpu_percent = True
c.NotebookApp.ResourceUseDisplay.cpu_limit = 8
```
