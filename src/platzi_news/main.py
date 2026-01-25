"""Main entry point for Platzi News."""

import asyncio

from .io.cli import main as async_main


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    linea para hacer uso de precommit y que valide una linea mayor a 88 caracteres que es el limente para usar en python y de como resultado un err
    main()
