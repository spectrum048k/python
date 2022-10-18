# Pyinstrument Demo

## Run locally

```sh
    # time app using terminal
    time python demo.py 

    # run app using pyinstrument
    pyinstrument demo.py

    # output pyinstrument results in html
    pyinstrument -r html demo.py
```

## Speedscope

Use [speedscope](https://www.speedscope.app/) for flamegraphs

```sh
   pyinstrument -r speedscope -o speedscope.json demo.py
```

## Inline profiler

Use pyinstrument from within your code:

```sh
python demo2.py
```