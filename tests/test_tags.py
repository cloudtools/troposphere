import unittest
from troposphere import Tags
from troposphere.autoscaling import Tags as ASTags


class TestTags(unittest.TestCase):
    def test_TagAddition(self):
        tags = Tags(foo='foo')
        tags += Tags(bar='bar')
        tags = tags + Tags(baz='baz')
        result = [
            {'Value': 'foo', 'Key': 'foo'},
            {'Value': 'bar', 'Key': 'bar'},
            {'Value': 'baz', 'Key': 'baz'},
        ]
        self.assertEqual(tags.to_dict(), result)

    def test_ASTagAddition(self):
        tags = ASTags(foo=('fooval', True))
        tags += ASTags(bar=('barval', False))
        tags = tags + ASTags(baz='bazval')
        result = [
            {'Value': 'fooval', 'Key': 'foo', 'PropagateAtLaunch': 'true'},
            {'Value': 'barval', 'Key': 'bar', 'PropagateAtLaunch': 'false'},
            {'Value': 'bazval', 'Key': 'baz', 'PropagateAtLaunch': 'true'},
        ]
        self.assertEqual(tags.to_dict(), result)


if __name__ == '__main__':
    unittest.main()
