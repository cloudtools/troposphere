import unittest
from troposphere import Sub, Tags
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

    def test_Unsortable(self):
        result = [{'Key': {'Fn::Sub': 'somestring'}, 'Value': 'val'}]
        tags = Tags({Sub('somestring'): 'val'})
        self.assertEqual(tags.to_dict(), result)

    def test_Formats(self):
        result = [
            {'Value': 'bar', 'Key': 'bar'},
            {'Value': 'baz', 'Key': 'baz'},
            {'Value': 'foo', 'Key': 'foo'},
        ]
        tags = Tags(bar='bar', baz='baz', foo='foo')
        self.assertEqual(tags.to_dict(), result)
        tags = Tags({'bar': 'bar', 'baz': 'baz', 'foo': 'foo'})
        self.assertEqual(tags.to_dict(), result)
        tags = Tags(**{'bar': 'bar', 'baz': 'baz', 'foo': 'foo'})
        self.assertEqual(tags.to_dict(), result)
        result = [{'Key': 'test-tag', 'Value': '123456'}]
        tags = Tags({'test-tag': '123456'})
        self.assertEqual(tags.to_dict(), result)

        with self.assertRaises(TypeError):
            Tags(1)
        with self.assertRaises(TypeError):
            Tags("tag")
        with self.assertRaises(TypeError):
            Tags("key", "value")
        with self.assertRaises(TypeError):
            Tags({}, "key", "value")


if __name__ == '__main__':
    unittest.main()
