import pandas as pd

def generate_report(results, output_file):
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"Отчёт сохранён в {output_file}")
