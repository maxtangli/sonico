<?php

/**
 * session hijacking attack:
 *  attacker may stole user's session id.
 * security strategy:
 * - use https.
 * - expire earlier.
 */

/**
 * session fixation attack:
 *  attack provide a url with uninitialized session id. e.g. http://example.org/test.php?PHPSESSID=1234
 *  user who accessed the url will use a session id chosen by attacker.
 * security strategy:
 * - session.use_only_cookies=1: to reject param transferred session ID.
 * - session.use_strict_mode=1: to reject uninitialized session ID.
 */

// session.auto_start: default 0.
/**
 * if session_id passed (by cookie or param):
 *  if session_handler.load session_id:
 *   $_SESSION = loaded data
 *   if session_handler is FILE:
 *    lock session_id
 *  else:
 *   ?
 * else:
 *  generate a new session ID
 */
session_start();

if (empty($_SESSION['count'])) {
    $_SESSION['count'] = 1;
} else {
    $_SESSION['count']++;
}
echo session_name(), "\n", session_id(), "\n", $_SESSION['count'], "\n";

// todo: know how frameworks handle session security

/**
 * serialize $_SESSION, pass it to session.save_handler
 * session.save_handler: default FILE in session.save_path, close to release per session_id lock.
 */
session_write_close();
echo session_save_path(), "\n";