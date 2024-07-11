const path = require('path');

module.exports = {
  resolve: {
    fallback: {
      "http": require.resolve("stream-http"),
      "https": require.resolve("https-browserify"),
      "crypto": require.resolve("crypto-browserify"),
      "url": require.resolve("url"),
      "process": require.resolve("process/browser"),
      "buffer": require.resolve("buffer")
    }
  },
};
