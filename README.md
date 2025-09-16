# cvstruct

A toolbox for representing, converting, and visualizing common data structures in 2D CV tasks (i.e. bbox, contours, masks, etc.).

## Installation

```
# Uninstall old versions
pip uninstall cvstruct
rm -fr ./build

# Select one of the versions below, you can not install both

# Install GUI version
pip install -e .[gui] --config-settings editable_mode=strict

# Install NON-GUI version
pip install -e .[no_gui] --config-settings editable_mode=strict
```