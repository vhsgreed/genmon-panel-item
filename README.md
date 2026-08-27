# genmon-panel-item

A minimal XFCE Generic Monitor (genmon) panel item that displays a live
one-line status from any Python source — this example renders a
cryptocurrency/gas price line with a sparkline.

## Panel setup (XFCE)

1. Install the genmon plugin: `sudo apt install xfce4-genmon-plugin`
2. Right-click panel → Panel → Add New Items → **Generic Monitor**
3. Properties:
   - Command: `python3 /path/to/ui_genmon.py`
   - Period: `60`
   - Label: (empty)
4. Use a monospace font so the sparkline stays aligned.

## How it works

The script is a thin wrapper: it imports a `panel_line(fetch_first=True)`
function from your data source module and prints its output. If anything
fails, it prints a short `err:` line instead of crashing the panel.

## Customizing

Swap the import to your own module — the contract is just:

```python
def panel_line(fetch_first: bool = False) -> str: ...
```

Returns a single line of text (optionally with unicode sparkline chars)
that genmon renders and auto-refreshes.
