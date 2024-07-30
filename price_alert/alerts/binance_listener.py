import asyncio
import json
import websockets
from django.conf import settings
from django.core.mail import send_mail
from .models import Alert
from django.utils import timezone

async def binance_listener():
    uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            price_data = json.loads(data)
            current_price = float(price_data['p'])
            alerts = Alert.objects.filter(cryptocurrency='BTC', status='created')
            for alert in alerts:
                if alert.target_price <= current_price:
                    alert.status = 'triggered'
                    alert.triggered_at = timezone.now()
                    alert.save()
                    send_mail(
                        'Price Alert Triggered',
                        f'The price of BTC has reached your target price of {alert.target_price}.',
                        settings.DEFAULT_FROM_EMAIL,
                        [alert.user.email]
                    )

def start_listener():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(binance_listener())
