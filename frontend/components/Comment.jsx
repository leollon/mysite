// components/Comments.jsx

import React from 'react';
import PropTypes from 'prop-types';

import CommentForm from './Forms';
import PageList from './Pagination';
import SyntaxHighlight from './SyntaxHighlight';

export default function Comments(props) {
    const statistics = props.statistics;
    const commentArray = props.comments.results;

    return (
        <div className="comment-content" id="comments">
            <p className="fa fa-comment">
                {' '}
                {statistics} Comment{statistics !== 1 ? 's' : ''}
            </p>
            <hr id="underline" />
            <ul id="comment-list">
                {commentArray.length ? (
                    commentArray.map((comment) => (
                        <li
                            className="comment"
                            key={comment.username + comment.created_time}
                        >
                            <a
                                href={comment.link ? comment.link : ''}
                                className="username"
                            >
                                {comment.username}
                            </a>
                            <span className="timestamp">
                                {' '}
                                @
                                <a href={'#' + comment.username}>
                                    {' '}
                                    {comment.created_time}
                                </a>{' '}
                                said:
                            </span>
                            <div className="comment-text">
                                <SyntaxHighlight
                                    content={comment.comment_text}
                                />
                            </div>
                            <span
                                className="reply"
                                data-commenter={comment.username}
                            >
                                Reply
                            </span>
                        </li>
                    ))
                ) : (
                    <li className="empty comment" key="empty-comment">
                        No Comments yet!
                    </li>
                )}
            </ul>
            <PageList links={props.comments.links} />
            <CommentForm slug={props.slug} post_id={props.id} />
        </div>
    );
}

Comments.propTypes = {
    id: PropTypes.number.isRequired,
    slug: PropTypes.string.isRequired,
    comments: PropTypes.object.isRequired,
    statistics: PropTypes.number.isRequired,
};
