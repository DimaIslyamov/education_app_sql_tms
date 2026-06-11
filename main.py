#!/usr/bin/env python3
"""Точка входа в приложение учебного портала."""

import sys

from cli.menu import PortalApp
from database.connection import Database


def run_cli() -> None:
    """Запустить консольный интерфейс."""
    with Database() as db:
        app = PortalApp(db)
        app.run()


def main() -> None:
    """Запустить приложение в выбранном режиме."""
    run_cli()

if __name__ == "__main__":
    main()