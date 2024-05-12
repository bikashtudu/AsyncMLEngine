from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging


logger = logging.getLogger(__name__)


class LoginConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_authenticated:
            self.room_group_name = f"user_{self.scope['user'].id}"
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.scope["user"].is_authenticated:
            await self.channel_layer.group_discard(
                self.room_group_name, self.channel_name
            )

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        if message == "Hello, server!":
            message = f"Hello {self.scope['user'].username}!"

        await self.send(text_data=json.dumps({"message": message}))

    async def task_message(self, event):
        message = event["message"]
        logger.warning(message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
