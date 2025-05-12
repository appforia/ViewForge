from viewforge.core.component import Component


class ShoelaceAvatar(Component):
    def __init__(self, initials=None, image=None, label=None, **props):
        self.initials = initials
        self.image = image
        self.label = label
        self._props = props
        super().__init__()

    def render(self):
        props = []
        if self.initials:
            props.append(f'initials="{self.initials}"')
        if self.image:
            props.append(f'image="{self.image}"')
        if self.label:
            props.append(f'label="{self.label}"')
        props += [f'{k}="{v}"' for k, v in self._props.items()]
        return f'<sl-avatar {" ".join(props)}></sl-avatar>'


class ShoelaceBadge(Component):
    def __init__(self, content: str, **props):
        self.content = content
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-badge {" ".join(f"{k}={v!r}" for k, v in self._props.items())}>{self.content}</sl-badge>'


class ShoelaceTag(Component):
    def __init__(self, content: str, **props):
        self.content = content
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-tag {" ".join(f"{k}={v!r}" for k, v in self._props.items())}>{self.content}</sl-tag>'


class ShoelaceDetails(Component):
    def __init__(self, summary: str, content: str, **props):
        self.summary = summary
        self.content = content
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-details {" ".join(f"{k}={v!r}" for k, v in self._props.items())}><div slot="summary">{self.summary}</div>{self.content}</sl-details>'


class ShoelaceAnimation(Component):
    def __init__(self, name: str, play: bool = True, **props):
        self.name = name
        self.play = play
        self._props = props
        super().__init__()

    def render(self):
        props = [f'name="{self.name}"', f'play={"true" if self.play else "false"}']
        props += [f'{k}="{v}"' for k, v in self._props.items()]
        return f'<sl-animation {" ".join(props)}></sl-animation>'


class ShoelaceAnimatedImage(Component):
    def __init__(self, src: str, alt: str = "", **props):
        self.src = src
        self.alt = alt
        self._props = props
        super().__init__()

    def render(self):
        props = [f'src="{self.src}"', f'alt="{self.alt}"']
        props += [f'{k}="{v}"' for k, v in self._props.items()]
        return f'<sl-animated-image {" ".join(props)}></sl-animated-image>'


class ShoelaceImageComparer(Component):
    def render(self):
        return '<sl-image-comparer></sl-image-comparer>'


class ShoelaceQRCode(Component):
    def __init__(self, value: str, **props):
        self.value = value
        self._props = props
        super().__init__()

    def render(self):
        props = [f'value="{self.value}"'] + [f'{k}="{v}"' for k, v in self._props.items()]
        return f'<sl-qr-code {" ".join(props)}></sl-qr-code>'


class ShoelaceRelativeTime(Component):
    def __init__(self, date: str, **props):
        self.date = date
        self._props = props
        super().__init__()

    def render(self):
        props = [f'date="{self.date}"'] + [f'{k}="{v}"' for k, v in self._props.items()]
        return f'<sl-relative-time {" ".join(props)}></sl-relative-time>'
