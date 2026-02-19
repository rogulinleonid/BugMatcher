import json
from youtrack_module import get_student_tickets
from google_sheets_module import get_reference_bugs
from matching_module import match_bugs
from report_module import generate_report

def main():
    with open('config.json') as f:
        config = json.load(f)
    
    # Шаг 1: Получаем тикеты
    student_bugs = get_student_tickets(
        config['youtrack']['url'],
        config['youtrack']['token'],
        config['youtrack']['project_id']
    )
    
    # Шаг 2: Получаем эталонные баги
    reference_bugs = get_reference_bugs(
        config['google_sheets']['url'],
        config['google_sheets']['sheet_name']
    )
    
    # Шаг 3: Сопоставляем
    results = match_bugs(student_bugs, reference_bugs)
    
    # Шаг 4: Формируем отчёт
    generate_report(results, config['report_output'])

if __name__ == "__main__":
    main()
