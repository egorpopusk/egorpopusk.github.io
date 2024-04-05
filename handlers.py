async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Тестируем WebApp',
                           reply_markup=keyboard)

PRICE = {
    '1': [types. LabeledPrice(label='Item1', amout=100000)],
    '2': [types. LabeledPrice(label='Item2', amout=200000)],
    '3': [types. LabeledPrice(label='Item3', amout=300000)],
    '4': [types. LabeledPrice(label='Item4', amout=400000)],
    '5': [types. LabeledPrice(label='Item5', amout=500000)],
    '6': [types. LabeledPrice(label='Item6', amout=600000)]
}
@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    await bot.send_invoice(web_app_message.chat.id,
                           title='Laptop',
                           description='Description',
                           provider_token='pay_token',
                           currency='rub',
                           need_email=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Платёж прошел успешно!')
