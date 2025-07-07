def test_true_is_true():
    assert True is True

# Örnek: model dosyasının varlığını test edelim
import os

def test_model_file_exists():
    assert os.path.isfile("model.pkl"), "model.pkl bulunamadı"