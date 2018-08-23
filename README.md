# agespysawrapper

> API wrapper para buscar contas de água do estado do Piauí pela AGESPISA.

[![PyPI version](https://badge.fury.io/py/pysinonimos.svg)](https://badge.fury.io/py/agespysawrapper)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Instalação:

```pip install agespysawrapper```

## Exemplos:

```
>>> from agespysawrapper.agespysa import Agespisa

>>> fulano = Agespisa("register_id")

>>> fulano
<register_id: XXXXXXX, name: FULANO DE TAL, debit_amount: 32.03>

>>> fulano.city
TERESINA

>>> fulano.debits
[<month: 2018-05-01, value: 30.00, link: www.agespisa.com.br/gsan/gerarRelatorio2ViaContaAction.do?cobrarTaxaEmissaoConta=N&idContaXXXXX>,
<month: 2018-06-01, value: 2.03, link: www.agespisa.com.br/gsan/gerarRelatorio2ViaContaAction.do?cobrarTaxaEmissaoConta=N&idContaXXXXX>,]

>>> type(fulano.debits[0].value)
<class 'decimal.Decimal'>
```

## Créditos:

> Diego Fernando
