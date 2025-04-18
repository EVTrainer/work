const mongoose = require("mongoose");

const genreSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  songs: {
    type: [{ type: mongoose.SchemaTypes.ObjectId, ref: "Song" }],
    default: [],
  },
});

module.exports = {
  genreModel: mongoose.model("Genre", genreSchema),
  genreSchema,
};
