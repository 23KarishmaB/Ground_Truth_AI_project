from src.preprocess import main as preprocess_main
from src.analyze import main as analyze_main
from src.generate_report import build_report

def main():
    print("=== Automated Insight Engine ===")
    preprocess_main()
    metrics, imgs = analyze_main()
    build_report(metrics, imgs)
    print("=== Pipeline finished. Check output/ ===")

if __name__ == "__main__":
    main()
