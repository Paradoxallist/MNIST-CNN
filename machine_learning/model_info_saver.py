def save_model_info(model, history, save_path):
    from datetime import datetime
    import os
    from common.config import EPOCHS, BATCH_SIZE, LEARNING_RATE

    final_val_accuracy = history.history['val_accuracy'][-1]
    final_val_loss = history.history['val_loss'][-1]

    model_summary = []
    model.summary(print_fn=lambda x: model_summary.append(x))
    model_structure = "\n".join(model_summary)

    info_text = f"""Model Information
===========================
Saved on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Training Settings:
- Epochs: {EPOCHS}
- Batch size: {BATCH_SIZE}
- Learning rate: {LEARNING_RATE}

Final Results:
- Final Validation Accuracy: {final_val_accuracy:.4f}
- Final Validation Loss: {final_val_loss:.4f}

Model Architecture:
{model_structure}
"""

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:  # <-- исправили здесь
        f.write(info_text)
    print(f"Model information saved to {save_path}")
