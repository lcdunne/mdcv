# mdcv

A python utility to convert a markdown CV into a static HTML page.

## Quickstart

Create a `_config.yaml` file like this:

```yaml
title: Your Name
description: "Some description"
connects:
  github: # Your github url
  linkedin: # Your LinkedIn url
template: minimal
fontName: Lato # Any google font
colours:
  context: "#eceff4"
  background: "#fffff"
  foreground: "#434c5e"
  highlight: "#5E81AC"
```

Make your you have a file, e.g. `cv.md` - this gets converted to HTML.
