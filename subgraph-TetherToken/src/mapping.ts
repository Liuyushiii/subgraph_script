// event
import { Transfer} from '../generated/TetherToken/TetherToken'
// entity
import { TokenTransfer} from '../generated/schema'

import {BigInt, bigInt, BigDecimal} from '@graphprotocol/graph-ts'


export function handleTransfer(event: Transfer): void {
  let id = event.params.from.toHexString()
  let transfer = new TokenTransfer(id)
  transfer.from_account = event.params.from.toHexString()
  transfer.to_account = event.params.to.toHexString()
  transfer.value = event.params.value
  transfer.save()
}