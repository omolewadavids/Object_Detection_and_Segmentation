import torch


class Metric:
    @classmethod
    def accuracy(cls, x, y, model):
        torch.no_grad()
        prediction = model(x)
        is_correct = (prediction > 0.5) == y
        return is_correct.cpu().numpy().tolist()

    @classmethod
    def val_loss(cls, x, y, model, loss_fn):
        torch.no_grad()
        prediction = model(x)
        val_loss = loss_fn(prediction, y)
        return val_loss.item()
