from src.preprocess import load_data, preprocess
from src.train_model import train_model
from src.evaluate import evaluate_model
import joblib
import os

def main():
    print("🔹 Bắt đầu chạy pipeline...")

    # 1. Load dữ liệu
    data_path = "data/Scholarship_Probability.csv"
    if not os.path.exists(data_path):
        print(f"❌ Không tìm thấy file: {data_path}")
        return

    print("✅ Đã load dữ liệu")
    df = load_data(data_path)

    # 2. Tiền xử lý
    print("🔧 Đang xử lý dữ liệu...")
    X, y, scaler = preprocess(df)

    # Lưu scaler
    os.makedirs("models", exist_ok=True)
    joblib.dump(scaler, "models/scaler.pkl")
    print("✅ Đã lưu scaler")

    # 3. Train mô hình
    print("🤖 Đang huấn luyện mô hình...")
    model, X_test, y_test = train_model(X, y, save_path="models/best_model.pkl")
    print("✅ Đã lưu mô hình Random Forest")

    # 4. Đánh giá
    print("📊 Đang đánh giá mô hình...")
    evaluate_model(y_test, model.predict(X_test))

    print("\n🎉 HOÀN TẤT! Mô hình đã sẵn sàng để dùng trong web app.")

if __name__ == "__main__":
    main()
