import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton
import pytest

# Import the code to be tested
from simple_factory import BlueLabel, NamerFactory, FirstFirst, LastFirst, Builder


def test_namer_classes():
    # Test parsing of First <space> Last names
    namer = FirstFirst("John Doe")
    assert namer.first == "John"
    assert namer.last == "Doe"

    # Test parsing of Last <comma> First names
    namer = LastFirst("Doe, John")
    assert namer.first.strip() == "John"
    assert namer.last.strip() == "Doe"

    # Test handling of single-word names
    namer = FirstFirst("John")
    assert namer.first == ""
    assert namer.last == "John"

    # # Test handling of invalid names
    # with pytest.raises(ValueError):
    #     FirstFirst("John Doe 123")  # Contains extra characters


def test_namer_factory():
    # Test correct Namer instance creation based on comma
    namer_factory = NamerFactory("John Doe")
    assert isinstance(namer_factory.get_namer(), FirstFirst)

    namer_factory = NamerFactory("Doe, John")
    assert isinstance(namer_factory.get_namer(), LastFirst)


def test_builder_class():
    app = QApplication(sys.argv)  # Needed for QWidget testing

    builder = Builder()

    # Test UI element creation
    assert isinstance(builder.entry, QLineEdit)
    assert isinstance(builder.first_name_edit, QLineEdit)
    assert isinstance(builder.last_name_edit, QLineEdit)
    assert isinstance(builder.bt_compute, QPushButton)
    assert isinstance(builder.bt_clear, QPushButton)
    assert isinstance(builder.bt_quit, QPushButton)

    # Test "Compute" button functionality
    builder.entry.setText("John Doe")
    builder.compute()
    assert builder.first_name_edit.text() == "John"
    assert builder.last_name_edit.text() == "Doe"

    # Test "Clear" button functionality
    builder.entry.setText("Jane Smith")
    builder.first_name_edit.setText("Jane")
    builder.last_name_edit.setText("Smith")
    builder.clear_panel()
    assert builder.entry.text() == ""
    assert builder.first_name_edit.text() == ""
    assert builder.last_name_edit.text() == ""


if __name__ == "__main__":
    pytest.main()
