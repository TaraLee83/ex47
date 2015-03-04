import textwrap



a_list = ["""You realized that you stood, staring into the millions of facets of those
eyes. They shimmered and dissected the bleak world around into beautiful
reflections.
"""]

ready_to_print = textwrap.dedent(a_list[0]).strip()
for width in [80]:
    print
    print textwrap.fill(ready_to_print, initial_indent='     ', subsequent_indent='', width=width)