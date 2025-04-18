"use strict";

// ==========================
// General Require Statements
// ==========================
const { Types } = require("mongoose");
const { userModel } = require("../models/User");
const { roleModel } = require("../models/Role");
const { commentModel } = require("../models/Comment");
const { listedSongModel } = require("../models/ListedSong");

// ==============================
// Endpoints for Posting Comments
// ==============================
const postComment = async (req, res) => {
  let listingId;
  try {
    listingId = new Types.ObjectId(req.params.id);
  } catch (error) {
    console.log(error);
    return res.status(400).json({ error: "Invalid listing ID" });
  }

  console.log(`Searching for listing with ID ${listingId}`);

  try {
    const listedSong = await listedSongModel.find({ _id: listingId }).exec();
    if (!listedSong) {
      return res.status(400).json({ error: "Invalid listing ID" });
    }
    if (!req.user) {
      return res.status(400).json({ error: "Invalid username" });
    }

    const foundUser = await userModel.findOne({ username: req.user }).exec();
    if (!foundUser) {
      return res.status(400).json({ error: "No user with username" });
    }

    const createdComment = await commentModel.create({
      listedSong: req.params.listingId,
      postedBy: foundUser._id,
      message: req.body.comment,
    });
    res.status(200).json({ message: "Comment Posted!" });
  } catch (error) {
    console.log(error);
    return res.status(400).json({ message: "Failed to post comment" });
  }
};

const getComment = async (req, res) => {
  //Check if commentID is provided
  let commentID = req.params.id;
  if (!commentID) {
    return res.status(400).json({ message: "No ID provided" });
  }
  try {
    // Get comment from database
    const queriedComment = await commentModel.findById(commentID).exec();
    if (!queriedComment) {
      return res.status(400).json({ error: "No such comment" });
    }
    return res.status(200).json({ result: queriedComment, message: "Success" });
  } catch (error) {
    console.log(error);
    return res
      .status(500)
      .json({ result: [], message: "Error getting comment" });
  }
};

const getComments = async (req, res) => {
  try {
    // Get comments from database
    const queriedComments = await commentModel.find({}).exec();
    if (!queriedComments) {
      return res.status(400).json({ error: "No comments in database" });
    }
    return res
      .status(200)
      .json({ result: queriedComments, message: "Success" });
  } catch (error) {
    console.log(err);
    return res
      .status(500)
      .json({ result: [], message: "Error getting comments" });
  }
};

const updateComment = async (req, res) => {
  try {
    let { commentid, comment } = req.body;
    if (!commentid || !comment) {
      return res
        .status(400)
        .json({ message: "Comment ID and comment are required" });
    }
    //Checks if comment exists
    let commentToUpdate = await commentModel.findById(commentid).exec();
    if (!commentToUpdate) {
      return res
        .status(400)
        .json({ result: null, message: "invalid comment ID" });
    }
    //Get user who requesting edit
    let originalPoster = await userModel.findOne({ username: req.user }).exec();
    if (!originalPoster) {
      return res.status(400).json({ result: null, message: "invalid User ID" });
    }
    //Gets all roles from database
    let clearanceLevel = await roleModel.findById(originalPoster["roles"][0]);
    if (!clearanceLevel) {
      return res.status(400).json({ result: null, message: "invalid Role ID" });
    }
    //Allow original poster or admin to edit comment
    if (
      String(commentToUpdate.postedBy) == String(originalPoster["_id"]) ||
      clearanceLevel["clearanceLevel"] == 2
    ) {
      let updatedComment = await commentModel
        .findByIdAndUpdate(
          commentid,
          { userid: originalPoster._id, message: comment },
          { new: true }
        )
        .exec();
      return res
        .status(200)
        .json({ result: updatedComment, message: "Success" });
    }
    //Rejection message for users without correct permissions
    return res.status(403).json({
      result: null,
      message: "Access Denied; You don't have permission to alter comment",
    });
  } catch (err) {
    console.log(err);
    return res
      .status(500)
      .json({ result: null, message: "Error updating comment" });
  }
};

const updateCommentState = async (req, res) => {
  try {
    const { commentid, flagStatus } = req.body;
    if (!flagStatus || !commentid) {
      console.log(commentid);
      console.log(flagStatus);
      console.log(roles);
      return res
        .status(400)
        .json({ result: null, message: "You need to fill all parameters" });
    }
    //Checks if comment exists
    let commentToUpdate = await commentModel.findById(commentid).exec();
    if (!commentToUpdate) {
      return res
        .status(400)
        .json({ result: null, message: "invalid comment ID" });
    }
    //Get user who requesting edit
    let originalPoster = await userModel.findOne({ username: req.user }).exec();
    if (!originalPoster) {
      return res.status(400).json({ result: null, message: "invalid User ID" });
    }
    //Gets all roles from database
    let clearanceLevel = await roleModel.findById(originalPoster["roles"][0]);
    if (!clearanceLevel) {
      return res.status(400).json({ result: null, message: "invalid Role ID" });
    }
    if (clearanceLevel["clearanceLevel"] != 2) {
      return res.status(403).json({
        result: null,
        message: "Access Denied; You don't have permission to alter comment",
      });
    }
    let updatedComment = await commentModel
      .updateOne({ _id: commentid }, { flagged: flagStatus })
      .exec();
    return res.status(200).json({ result: updatedComment, message: "Success" });
  } catch (err) {
    console.log(err);
    return res
      .status(500)
      .json({ result: null, message: "Error updating comment" });
  }
};

const deleteComment = async (req, res) => {
  //Checks if ID is provided
  const commentID = req.body.commentid;
  if (!commentID) {
    return res.status(400).json({ message: "No ID provided" });
  }
  try {
    //Checks if comment exists in database
    let commentExists = await commentModel.findById(commentID);
    if (!commentExists) {
      return res
        .status(400)
        .json({ result: null, message: "invalid comment ID" });
    }
    //Get original poster of comment
    let originalPoster = await userModel.findOne({ username: req.user }).exec();
    if (!originalPoster) {
      return res.status(400).json({ result: null, message: "invalid User ID" });
    }
    //Get list of roles
    let clearanceLevel = await roleModel.findById(originalPoster["roles"][0]);
    if (!clearanceLevel) {
      return res.status(400).json({ result: null, message: "invalid Role ID" });
    }
    //Allows original poster or admin to delete comment
    if (
      String(commentExists.postedBy) == String(originalPoster["_id"]) ||
      clearanceLevel["clearanceLevel"] == 2
    ) {
      const deleteComment = await commentModel
        .findByIdAndDelete(commentID)
        .exec();
      return res.status(200).json({ result: null, message: "Success" });
    }
    //Rejection message for users without correct permissions
    return res.status(403).json({
      result: null,
      message: "Access Denied; You don't have permission to alter comment",
    });
  } catch (error) {
    console.log(error);
    return res
      .status(500)
      .json({ result: [], message: "Error deleting comment" });
  }
};

module.exports = {
  postComment,
  getComment,
  getComments,
  updateComment,
  deleteComment,
  updateCommentState,
};
