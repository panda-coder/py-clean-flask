#!/usr/bin/env python3

from main.config import app

from domain.dtos import SumDTO
from use_case import SumAction


if __name__ == '__main__':
    app.server.run(debug=True, host='0.0.0.0', port=3000)