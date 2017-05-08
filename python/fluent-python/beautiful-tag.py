# example of flexible function parameter handling
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

if __name__=='__main__':
    a = [
        tag('br'),
        tag('p', 'hello'),
        tag('p', 'hello', 'world'),  # implode variables into *content
        tag('p', 'hello', id=13),  # implode pairs into **attrs
        tag('p', 'hello', 'world', cls='sidebar'),
        tag(**{'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'})
    ]
    for i, s in enumerate(a):
        print(i)
        print(s)
